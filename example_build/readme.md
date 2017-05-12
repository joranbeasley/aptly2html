you can generate data with aptly using

`aptly show package "(Version)" > my_input_file.dat` 


in my example I use [`example_aptly_show.dat`](./example_aptly_show.dat) as the file


you can, and should, specify a welcome file that tells a user how to add your aptly repository to their apt-list.


I use [`install_directive.md`](./install_directive.md) in my example

we now have everything we need to build our html page

`aptly2html --infile=example_aptly_show.dat --index=install_directive.md > example_output.html`

and we have now generated an example single page application [`example_output_site.html`](./example_output.html)

### [View Generated Site](https://joranbeasley.github.io/aptly2html/example_build/example_output.html)

of coarse we could have done this with a direct pipe as well

`aptly show package "(Version)" | aptly2html --stdin --index=install_directive.md > example_output.html`