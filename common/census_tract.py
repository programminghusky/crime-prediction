
def formatTractName(tractName):
    # Find the first occurrence of comma or semicolon
    comma_pos = tractName.find(',')
    semicolon_pos = tractName.find(';')
    
    # If neither delimiter is found, return the entire string
    if comma_pos == -1 and semicolon_pos == -1:
        return tractName
    
    # If only one delimiter is found, use that position
    if comma_pos == -1:
        return tractName[:semicolon_pos]
    if semicolon_pos == -1:
        return tractName[:comma_pos]
    
    # If both delimiters are found, use the one that appears first
    first_delimiter_pos = min(comma_pos, semicolon_pos)
    return tractName[:first_delimiter_pos]

def formatTractGroupName(tractName):
    dot_pos = tractName.find('.')
    if dot_pos == -1:
       return tractName
    return tractName[:dot_pos]