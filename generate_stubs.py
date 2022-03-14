from pathlib import Path
from typing import List, Literal, NamedTuple, Tuple
import jinja2
import mozilla
import tqdm

template = jinja2.Template(
    """class {{tag | title | replace("-", "")}}(Node):
    \"\"\"
    {{url}}
    \"\"\"
    @overload
    def __call__(
        self,
        {% if attributes %}*,{% endif %}
        {% for attr in attributes -%}
        {{attr | replace("-", "") | replace(":", "__")}} = None,
        {% endfor -%}
        **attrs,
    ) -> "{{tag | title | replace("-", "")}}":  # type: ignore
        \"\"\"
        `<{{tag}}{% for attr in attributes %} {{attr}}{% endfor %} />` [(docs)]({{url}})
        {% if example %}

        Example:
        ```
        {{example | indent(8, False) | trim }}
        ```
        {% endif -%}
        \"\"\"
        pass

    @overload
    def __call__(
        self,
        *children: Union[Node, str, Generator[Union[Node, str], None, None]],
    ) -> "{{tag | title | replace("-", "")}}":  # type: ignore
        \"\"\"
        `<{{tag}}{% for attr in attributes %} {{attr}}{% endfor %} />` [(docs)]({{url}})
        {% if example %}

        Example:
        ```
        {{example | indent(8, False) | trim}}
        ```
        {% endif -%}
        \"\"\"

    def __call__(*args, **kwargs) -> "{{tag | title | replace("-", "")}}":  # type: ignore
        pass


{{tag | replace("-", "_")}}: {{tag | title | replace("-", "")}} = Node("{{tag}}")  # type: ignore



"""
)


def main():
    all_tags = mozilla.all_svg_elements()

    outfile = Path(__file__).parent / "domtree" / "svg_stubs.py"
    with open(outfile, "w") as fp:
        fp.write(
            f"# This file was auto-generated by {__file__}.\n\n"
            f"from typing import overload, Callable, Dict, List, Any, Optional, Union, Generator\n"
            f"from domtree.node import Node\n\n"
        )

        for i, tag in enumerate(tqdm.tqdm(all_tags)):
            page = mozilla.look_up_svg_page(tag)
            fp.write(
                template.render(
                    tag=tag,
                    example=page.examples[0] if len(page.examples) > 0 else None,
                    url=page.url,
                    attributes=page.attributes,
                )
            )


if __name__ == "__main__":
    main()
