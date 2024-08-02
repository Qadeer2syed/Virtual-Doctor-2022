import inspect

x, malaria, z = 1, 2, 3

def retrieve_name(var):
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    return [var_name for var_name, var_val in callers_local_vars if var_val is var]

print(retrieve_name(malaria),retrieve_name(x),retrieve_name(z))

p = 1
print(retrieve_name(1))

