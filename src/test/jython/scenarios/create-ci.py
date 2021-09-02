from asserts import assert_true
from variables import *

repository.create(factory.configurationItem(my_ci_id, 'udm.Application'))
assert_true(repository.exists(my_ci_id))
