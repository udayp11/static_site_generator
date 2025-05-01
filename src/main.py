import os
import shutil
import sys


from htmlnode import HTMLNode
from split_delimiter import (split_nodes_delimiter,
                        extract_markdown_images,
                        extract_markdown_links,
                        split_nodes_image,
                        split_nodes_link,
                        text_to_textnodes)
from markdown_to_blocks import (markdown_to_blocks,markdown_to_html_node)

from generatepage import generate_pages_recursive

from textnode import (TextNode, TextType)



dir_path_static = "./static"
#dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"
dir_path_docs = "./docs"



def main():
    

    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:        
        basepath = "/"

    print("Deleting docs directory...")
    if os.path.exists(dir_path_docs):
        shutil.rmtree(dir_path_docs)

    print("Copying static files to docs directory...")
    files_source_to_dest(dir_path_static, dir_path_docs)

  

    print("Generating content...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_docs,basepath)


def files_source_to_dest(source_dir,dest_dir):

    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    
    os.mkdir(dest_dir)

    for item in os.listdir(source_dir):
        source_path = os.path.join(source_dir,item)
        dest_path = os.path.join(dest_dir,item)

        if os.path.isfile(source_path):
            print(f"Copying file {source_path} to {dest_path}")
            shutil.copy(source_path,dest_path)

        else:
            print(f"Copying directory {source_path} to {dest_path}")
            files_source_to_dest(source_path,dest_path)




main()