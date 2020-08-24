Plotting Recommendations for Journal Papers
#######################

Written by Pouria, added to Github by Christian

Figure Size: 
==========
Try to use 3.25” figure width, but height can vary depending on the figure;
however, it is usually recommended to use smaller value for height (use 2.25” for first
attempt). Note that square plots are not desirable in general. If you have multicolumn
figures then use a 6.5" wide figure. Note that these numbers are a good point to start, but
you may need to adjust the size based on your specific figure.

Font Type:
==========
Size: use “Arial” for font type (default in MATLAB) with font size 10 for
labels and titles, 8 for tick labels, and 8 for legends in journal papers. Remember that
journal don&#39;t let you plot anything below 8-pt font size.

Line Colors: 
==========
Usually best to use black if you are only plotting one curve. With multiple
curves, try not to use bright colors. Use this website to figure out what colors to use:
http://colorbrewer2.org. In MATLAB, you have to specify line colors in the format of
RGB percentages. As an example, the RGB color codes for the most used line colors are:
black ([0, 0, 0]), gray ([0.69, 0.69, 0.69]), and red ([0.839, 0.153, 0.157]).

Line Size and Style: 
==========
It is usually appropriate to set line widths of curves to 2, and line
styles can be "-", "--", "-.", ":". Note that some journals and authors have strong preference
for black and white colors only.

Legends:
==========
It is usually better to place the legends inside the plotting area but sometimes
they need to go outside. In this case, turn off the legend box.

Borders: 
==========
Use thick borders around for the figure’s outline. Set the line width for the
borders should to be 1.25 pt.

Grids: 
==========
Generally not needed; however, it might be useful in some cases depending on the
plot. Moreover, for some plots it might be helpful to draw the lines along the x- and y-
axes. You can probably use gray color ([0.8, 0.8, 0.8]) for them.

Exporting: 
==========
It is recommended to export plots as PNG file with a resolution of 300 dpi for
journal publications. SVG files are also nice if you want to keep data as a vector.

Title: 
==========
For the figures should go below. For the figure title, use same font type and size as
main body but with Bold text.
