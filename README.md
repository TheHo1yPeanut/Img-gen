# Img-gen
Very simple python program to generate basic shapes
<hr>
<h2>Shapes:</h2>
<ul>
  <li>Square</li>
  <li>Circle</li>
  <li>Star</li>
  <li>Composite shape: skull</li>
</ul>
<p>To create the shapes they all need to be given a position given as a tuple as well as a color. The star and the square also need a size. The circle need to be given a radius. Here are the syntaxes:</p>
<h2>STAR1 = star((xPos, yPos), rad, (r, g, b, a))</h2>
<h2>CIRCLE1 = circle((xPos, yPos), rad, (r, g, b, a))</h2>
<h2>SQUARE1 = square((xPos, yPos), size, (r, g, b, a))</h2>
<h2>SKULL1 = skull((xPos, yPos), (r, g, b, a))</h2>
<p>To create an image you will need to do "PICTURENAME = Picture()" and then add as many layers as you want to add shapes with "PICTURENAME.addLayer()". To add shapes use "PICTURENAME.addShape(SHAPENAME)". To return picture use "main.show()" in the end.</p>
