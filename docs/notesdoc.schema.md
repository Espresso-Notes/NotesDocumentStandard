# Espresso Notes Document

*A Notes Document to be utilized by the various modules of the Espresso Notes application.*

## Properties

- **`documentID`** *(string)*: A unique identifier for this document.
- **`title`** *(string)*: The title of this document.
- **`author`** *(string)*: The author of this document.
- **`lastModified`** *(integer)*: The date of the last modification of this document.
- **`content`** *(array)*: A list of all of the content blocks for this document.
  - **Items** *(object)*
    - **`blockType`** *(string)*: The type of the content block.
    - **`content`** *(string)*: The raw string of the content stored in this block.
