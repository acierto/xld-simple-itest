from variables import *

if repository.exists(my_ci_id):
    repository.delete(my_ci_id)
