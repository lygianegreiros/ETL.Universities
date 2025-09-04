from src.extract import extract
from src.load import load

Extract = extract()
Load = load()

br = Extract.extract_data("Brazil")
Load.load_data("universities", "universities_br", br)

it = Extract.extract_data("Italy")
Load.load_data("universities", "universities_it", it)
