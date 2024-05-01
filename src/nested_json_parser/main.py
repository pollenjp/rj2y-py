import json
import sys
import textwrap
import typing as t
from pathlib import Path

import click

YamlGeneralValueType: t.TypeAlias = int | str | bool | t.Mapping[t.Any, t.Any] | t.Iterable[t.Any]


def parse_nested_json(obj: YamlGeneralValueType) -> str:
    """文字列として埋め込まれている JSON もパースして表示する. YAML書式として出力する.

    Args:
        obj (YamlGeneralValueType): _description_

    Returns:
        str: _description_
    """
    prefix = "  "
    list_start = "-"
    list_prefix = "  "

    text_list: list[str] = []
    if isinstance(obj, str):
        # 可読性重視のため json 文字列の場合は、json としてパースする
        value: str | t.Any = obj
        if obj.lstrip().startswith("{") or obj.lstrip().startswith("["):
            # if encoded json string, parse it
            try:  # json check
                value = json.loads(obj)
            except json.JSONDecodeError:
                pass

        if isinstance(value, str):
            if len(value.split("\n")) <= 1:
                text_list.append(value)
            else:
                text_list.append("!!str |")
                text_list.append(value)
        else:
            text_list.append(textwrap.indent(parse_nested_json(value), prefix=prefix))
    elif isinstance(obj, t.Mapping):
        for k, v in obj.items():
            text_list.append(f"{k}:")
            if len((txt := parse_nested_json(v)).split("\n")) <= 1:
                text_list.append(text_list.pop() + f" {txt}")
            else:
                text_list.append(textwrap.indent(txt, prefix=prefix))
    elif isinstance(obj, t.Iterable):
        for v in obj:
            if len((txt := parse_nested_json(v)).split("\n")) <= 1:
                text_list.append(f"{list_start} {txt}")
            else:
                text_list += [
                    f"{list_start}",
                    textwrap.indent(parse_nested_json(v), prefix=list_prefix),
                ]
    else:
        text_list.append(f"{obj}")
    return "\n".join(text_list)


@click.command()
@click.argument("json_file", type=click.File("r"), default=sys.stdin)
def main(json_file: t.TextIO) -> None:
    """Parse JSON file to YAML. This command can also parse JSON string embedded in a string."""
    data: YamlGeneralValueType
    with json_file as f:
        data = json.load(f)

    click.echo(parse_nested_json(data))


if __name__ == "__main__":
    main()
