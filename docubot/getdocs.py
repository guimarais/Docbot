"""
Modules to get some documentation to explore with the chatbot
"""
from urllib.request import urlretrieve


def get_taxonomy(filename, language='EN', directory='./downloads'):
    """
    Downloads the taxonomy document into a local directory
    """

    # Target url
    url = f"https://eur-lex.europa.eu/legal-content/{language}/TXT/PDF/?uri=OJ:L_202302486"

    # Define the destination filename and get the document
    destination_filename = directory + "/" + filename
    urlretrieve(url, destination_filename)
    