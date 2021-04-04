# breakpoint(*args, **kws)
# This function drops you into the debugger at the call site. Specifically, it calls sys.breakpointhook(),
# passing args and kws straight through. By default, sys.breakpointhook() calls pdb.set_trace() expecting no arguments.
# In this case, it is purely a convenience function
# so you don’t have to explicitly import pdb or type as much code to enter the debugger.
# However, sys.breakpointhook() can be set to some other function and breakpoint() will automatically call that,
# allowing you to drop into the debugger of choice.

#while in PDB; Q to quit, C to continue...

#article about how to change the PDB default debugger with different debugger: https://www.journaldev.com/22695/python-breakpoint

"""
breakpoint(...)
    breakpoint(*args, **kws)

    Call sys.breakpointhook(*args, **kws).  sys.breakpointhook() must accept
    whatever arguments are passed.

    By default, this drops you into the pdb debugger.
"""


for i in range(10):
    print(i)
    if i == 5:
        breakpoint()
