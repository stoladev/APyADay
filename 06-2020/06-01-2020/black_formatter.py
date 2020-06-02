"""
Using the Black formatter, it seems that the formatting it provides is not as
useful as yapf.

I have switched to using yapf as a formatter alongside pylint as my Python
default linter. Coupling these two with COC and a few settings changed within
schema.json (through COC) proves to be useful.

My next steps should be to clean up Vim's Plugs that find little to no usable
benefit, similar to how Neoformat became obsolete once COC was configured
accordingly.

Check for the benefits of leaving in Neomake, polygot, pydocstring, and similar
plugins, weighing their actual use-cases as opposed to unnecessary clutter.
"""
