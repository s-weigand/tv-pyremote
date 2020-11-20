"""Update ``asset_src/dev_page.html`` can be invoked with ``npm run update``.

This is used to be able to use the parcel server for frontend development.
"""
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

from tv_pyremote.consts import DEV_PORT, roles


def render_frontend_dev_template():
    """Render the template for fronted development."""
    asset_src_path = Path(__file__).parent.parent
    template_dir = asset_src_path / "../tv_pyremote/templates"
    env = Environment(loader=FileSystemLoader(str(template_dir.resolve())))
    template = env.get_template("index.html")
    context = {"frontend_dev": True, "roles": roles, "dev_port": DEV_PORT}
    dev_page_string = template.render(context=context)
    dev_page_path = asset_src_path / "dev_page.html"
    dev_page_path.write_text(dev_page_string)


if __name__ == "__main__":
    render_frontend_dev_template()
