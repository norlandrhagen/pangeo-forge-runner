# Validate rewriting works in the presence of multiple aliased imports
import apache_beam as random_name_because_why_not
import apache_beam as random_name_because_why_not_second_fucking_time
from pangeo_forge_recipes.patterns import pattern_from_file_sequence

pattern = pattern_from_file_sequence(["hi.nc"])

recipe = random_name_because_why_not.Create(pattern.prune().items())
recipe = random_name_because_why_not_second_fucking_time.Create(pattern.prune().items())
