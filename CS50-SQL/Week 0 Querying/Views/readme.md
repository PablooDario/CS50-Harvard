# Schema

In `views.db` you’ll find a single table, views. In the views table, you’ll find the following columns:

- `id`, which uniquely identifies each row (print) in the table
- `print_number`, which identifies the number of the print in either Hokusai’s or Hiroshige’s series
- `english_title`, which is the English title of the print
- `japanese_title`, which is the Japanese title of the print
- `artist`, which is the last name of the print’s artist
- `average_color`, which is the hexadecimal representation of the color found by averaging the colors of each pixel in the image
- `brightness`, which is a number corresponding to the overall lightness or darkness of the image
- `contrast`, which is a number representing the extent of the difference between light and dark areas of the image
- `entropy`, which is a measure used to quantify the complexity of the artwork