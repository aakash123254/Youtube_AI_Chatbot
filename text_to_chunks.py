from langchain.document_loaders import TextLoader, DirectoryLoader 
from langchain.text_splitter import RecursiveCharacterTextSplitter 

def transcribed_text_to_chunks(url):
    """
        Convert all text files in a directory into smaller chunks for rmbeddings.
        
        Args:
            url (str): Directory path conatining .txt files. 
            
        Returns: 
            document (list): Loaded text documents.
            chunks (list): Text chunks after splitting.
    """
    # Load all the .txt files in the directory 
    loader = DirectoryLoader(
        url,
        glob = '*.txt',
        loader_cls = TextLoader
    )
    
    documents = loader.load()
    
    #Split text into smaller chunks for embeddings/vectorstore 
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 200,
        chunk_overlap = 60 
    )
    
    chunks = text_splitter.split_documents(documents)
    return documents, chunks 
