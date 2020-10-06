import re

def remove_punctuation(text, punctuation_to_space=False):
  """Removes all puncuation from a string. 
  If punctuation_to_space is set to True, puncuation are replace by spaces."""
  
  if punctuation_to_space:
    return re.sub(r"[^a-zA-Z0-9]"," ", text)
  else:
    return re.sub(r"[^a-zA-Z0-9]","", text)
  
  
