How to represent images: [pillow library](https://pillow.readthedocs.io/)
But why not let the user choose?
Proxy class which supports downloading and uploading images as [binary streams](https://docs.python.org/3/library/io.html#binary-i-o)

Use [python property attributes](https://docs.python.org/3/library/functions.html#property) to save and write values, i.e. `table[0].name = "Roel"`

Or make it more explicit by methods, i.e. `table[0].name.set("Roel")`

We can buffer writes or make them imediately.

Should we read the complete inspection, or on-demand?
Let the user decide.

For adding and removing assets we can emulate a [container type](https://docs.python.org/3/reference/datamodel.html#emulating-container-types) `__getitem__`, `__setitem__` and `__delitem__`

Repeating answers can be modelled as arrays of integers or strings.

Type classes and fields using [type hints](https://docs.python.org/3/library/typing.html#module-typing).

