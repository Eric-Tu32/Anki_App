from PyPDF2 import PdfReader
import re
import os

def main(*args):
    try:
        pdf_file_path = args[0]
        output_directory = args[1]

        base_name = os.path.splitext(os.path.basename(pdf_file_path))[0]
        output_md_filename = base_name + ".md" # Removes the file extension
        output_md_path = os.path.join(output_directory, output_md_filename)

        reader = PdfReader(pdf_file_path)
        text = ""

        for page in reader.pages: 
            text += page.extract_text() + "\n"


        pattern = r'(\d+)\.(.+?)(?=\n\d+\.|\Z)'
        matches = re.findall(pattern, text, re.DOTALL)
        #re.DOTALL 可以跨多行配對


        # Open a file in write mode
        with open(output_md_path, "w", encoding="utf-8") as md_file:
            for match in matches:
                question, options_block = match[0], match[1]
                question = question.strip()
                options_block = options_block.strip()

                options = re.split(r'\s+(?=[A-E]\.)', options_block)  # Add space for consistent splitting
                options = [opt.strip() for opt in options if opt]  # Remove empty strings and strip whitespace
            
                options[0] = options[0].replace("\n", " ")
                # Format the question with "##" in front and write to file
                formatted_question = "## " + question + ". " + options[0] 

                options = options[1:]
                # Write the options, ensuring no space before "A"
                for option in options:
                    if option.startswith(" A."):
                        option = option[1:]  # Remove the first character, which is the unwanted space
                    option = option.replace("\n", " ") 
                    formatted_question +=  "<br>"+ option 
                    
                md_file.write(formatted_question + "\n")
        
        return f"輸出成功：寫入{len(matches)}題"
    
    except Exception as e:
        return e







"""#在終端機顯示
for match in matches:

    question, options_block = match[0], match[1]
    question = question.strip()
    options_block = options_block.strip()
    print(options_block)
    options = re.split(r'\s+(?=[A-E]\.)', options_block) # Add space for consistent splitting
    options = [opt.strip() for opt in options if opt]  # Remove empty strings and strip whitespace

    # Format and print the question with "##" in front
    period_pos = question.find('.')
    formatted_question = "##" + question[period_pos + 1:] + "\t" + options[0]
    print(formatted_question)

    options = options[1:]
    # Print the options, ensuring no space before "A"
    for option in options:
        # If the option starts with a space followed by "A.", remove the space
        if option.startswith(" A."):
            option = option[1:]  # Remove the first character, which is the unwanted space
        print(option)
    
    print("---\n")  # Separator for readability"""