from mako.lookup import TemplateLookup
from os.path import abspath, dirname
from glob import glob

PATH = dirname(abspath(__file__))

MAKOLOOKUP = TemplateLookup(
    directories=PATH,
    disable_unicode=True,
    encoding_errors='ignore',
    default_filters=['str', 'h'],
    input_encoding='utf-8',
    output_encoding=''
)


def render(htm, **kwds):
    mytemplate = MAKOLOOKUP.get_template(htm)
    return mytemplate.render(**kwds)


for filename in glob("*.template"):
    prefix = filename.rsplit(".", 1)[0]
    with open("%s.js"%prefix,"w") as out:
        out.write(render(filename))
