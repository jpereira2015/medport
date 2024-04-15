import bz2

def decompress_bz2_chunked(input_path, output_path, chunk_size=1024*1024):  # Default chunk size is 1 MB
    # Open the .bz2 file
    with bz2.open(input_path, 'rb') as file:
        # Open the output file
        with open(output_path, 'wb') as output_file:
            # Read and write in chunks
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break
                output_file.write(chunk)

# Specify the path to your .bz2 file and the output file name
input_path = '/content/drive/MyDrive/Colab_files/ptwiki-20240401-pages-articles-multistream.xml.bz2'
output_path = '/content/drive/MyDrive/Colab_files/output_file.xml'

# Call the function to decompress the file
decompress_bz2_chunked(input_path, output_path)
import mwparserfromhell
import xml.etree.ElementTree as ET
import re

def clean_wikicode(text):
    wikicode = mwparserfromhell.parse(text)
    clean_text = wikicode.strip_code().strip()
    # Regex to clean up additional unwanted markup and text
    clean_text = re.sub(r'\[\[(File|Image|Archivo|Ficheiro):[^\]]+\]\]', '', clean_text, flags=re.IGNORECASE)
    clean_text = re.sub(r'(\d{1,4}px|miniaturadaimagem|thumb|thumbnail|direita|esquerda|centro)[\|_]', '', clean_text, flags=re.IGNORECASE)
    clean_text = re.sub(r'\[http[^\]]+\]', '', clean_text)
    clean_text = re.sub(r'\[\[Categoría:[^\]]+\]\]', '', clean_text, flags=re.IGNORECASE)
    clean_text = re.sub(r'{{[^}]+}}', '', clean_text)
    return clean_text

def process_xml_in_batches(file_path, output_path):
    context = ET.iterparse(file_path, events=("start", "end"))
    context = iter(context)
    event, root = next(context)

    with open(output_path, 'w', encoding='utf-8') as output:
        page_count = 0
        while True:
            try:
                event, elem = next(context)
                if event == "end" and elem.tag.endswith("page"):
                    title_elem = elem.find('.//{http://www.mediawiki.org/xml/export-0.10/}title')
                    text_elem = elem.find('.//{http://www.mediawiki.org/xml/export-0.10/}revision/{http://www.mediawiki.org/xml/export-0.10/}text')
                    
                    if title_elem is not None and text_elem is not None and text_elem.text:
                        title = title_elem.text
                        cleaned_text = clean_wikicode(text_elem.text)
                        output.write(f"Title: {title}\n{cleaned_text}\n\n")
                    
                    elem.clear()  # Clear processed element
                    root.clear()  # Also clear references from the root to the processed elements

                    page_count += 1
            except StopIteration:
                break  # Exit the loop if no more elements

        print(f"Processed {page_count} pages in total.")

# Specify your file paths here
input_xml_path = '/content/drive/MyDrive/Colab_files/output_file.xml'
output_txt_path = '/content/drive/MyDrive/Colab_files/output_file.txt'

# Start the batch processing
process_xml_in_batches(input_xml_path, output_txt_path)

##See just the first few lines of the text 

def sample_text_file(file_path, num_lines=40):
    """ Function to read and print the first 'num_lines' lines of a text file. """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for _ in range(num_lines):
                line = file.readline()
                if not line:
                    break
                print(line, end='')  # Use end='' to avoid double newlines
    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the path to your text file
file_path = 'output.txt'

# Call the function to sample the first 10 lines of the file
sample_text_file(file_path)
