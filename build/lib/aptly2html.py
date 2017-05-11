import json
import sys

from aptly2json import parse_packages

if __name__ == "__main__":

   from jinja2 import Environment, PackageLoader
   import argparse

   parser = argparse.ArgumentParser(description="parse input from `aptly package show` into a single file html application",
                                    usage="\n `python -m aptly2json -f some_input.txt`\n  - or - \n`aptly package show \"(Version >=0)\" | python -m aptly2json -I`")
   grp = parser.add_mutually_exclusive_group()
   grp.add_argument("-I", "--stdin", help="read package input from stdin", action='store_true', )
   grp.add_argument("-f", "--infile", help="read package input from a specified file", type=file)
   parser.add_argument("--index",help="a .md (markdown) or .html file to serve as the welcome message",type=file)
   args = parser.parse_args()
   if args.stdin is False and args.infile is None:
       parser.print_help(sys.stderr)
       parser.error('exactly one of `--stdin` or `--infile=<fname>` is required')
   elif args.stdin and not args.infile:
       args.infile = sys.stdin
   #parser.print_help()

   env = Environment(
       loader=PackageLoader('aptly2html_data', 'templates'),

   )
   welcome_msg = None
   raw_json = json.dumps(parse_packages(args.infile.read()))
   if args.index:
       if args.index.name.endswith(".md"):
           import markdown
           welcome_msg = markdown.markdown(args.index.read())
       else:
           welcome_msg = args.index.read()

   #
   # def docker_exec(container, cmd):
   #     return os.popen("docker exec -i %s %s" % (container, cmd)).read()

   template = env.get_template('index.html')
   ctx={
       'raw_json':raw_json,
       'welcome_msg':welcome_msg
   }
   print template.render(**ctx)
   #results =  docker_exec("aptly",'aptly package show "Version (>=0)"')
   # parse_packages(open("D:\\tmp\\simple.txt").read())
