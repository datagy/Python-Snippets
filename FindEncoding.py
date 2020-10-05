def find_encoding(file_path):
  """Requires Python 3.6 or higher."""
  from encodings.aliases import aliases

  alias_values = set(aliases.values())
  encodings = []
  for alias in alias_values:
      try:
          pd.read_csv(f'{file_path}', encoding=alias)
          encodings.append(alias)
      except: UnicodeDecodeError
  return encodings
