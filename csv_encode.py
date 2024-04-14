import csv
import re
import time  # Import the time module

def clean_wiki_markup(text):
    text = re.sub(r'\[\[(?:[^\]|]*\|)?([^\]|]+)\]\]', r'\1', text)  # Simplify links
    text = re.sub(r'<[^>]+>', '', text)  # Remove HTML-like tags
    text = re.sub(r'&lt;.*?&gt;', '', text)  # Remove HTML entities
    return text

csv_file = '/Users/josephpereira/medport/port_terms_utf8_file.csv'
wiki_dump_file = '/Users/josephpereira/medport/ptwiki-20240401-pages-articles-multistream.xml'
output_csv_file = '/Users/josephpereira/medport/setences.csv'

with open(csv_file, 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    with open(output_csv_file, 'w', encoding='utf-8', newline='') as output_csv:
        csv_writer = csv.writer(output_csv)
        csv_writer.writerow(["Term", "Example Sentence"])
        
        for row in csv_reader:
            term = row[0].strip()
            sentence_pattern = re.compile(r'\b([A-Z][^.?!]*?\b{}\b[^.?!]*[.?!])'.format(re.escape(term)), re.IGNORECASE)
            found_sentence = False
            
            with open(wiki_dump_file, 'r', encoding='utf-8') as wiki_dump:
                for line in wiki_dump:
                    if term.lower() in line.lower():
                        match = sentence_pattern.search(line)
                        if match:
                            example_sentence = match.group(0)
                            example_sentence = clean_wiki_markup(example_sentence)
                            csv_writer.writerow([term, example_sentence])
                            found_sentence = True
                            break
                
                if not found_sentence:
                    csv_writer.writerow([term, "NA"])
            
            time.sleep(1.0)  # Sleep after processing each term, for a brief pause
