# Algorithm code generation

1. Do topological sort on relationships of asset types to avoid undefined symbols.
   Partially correct: sort asset types by ones without and with relationships.

1. For each asset type:
   1. Create enumerations for single and repeateable property as Flag enumerations
   2. Write out fieldName --> property id dicts with all non-image properties.
   3. Write out rows as data class.
      1. For numbers and text with multiple answers, use `field(default_factory=list)`
      2. For images:
         1. Create a private backing attribute as
            `field(default_factory=lambda: ImageField(UUID("c6e25e1a-d182-404c-bd89-529808f51ee8")))`
         1. Create a read-only property.
      3. Write out table

All property names are snake cased.

# Misc

- Perhaps it is better to have the property dictionaries in a different file because they are quite noisy.
