# rj2y

[![PyPI](https://img.shields.io/pypi/v/rj2y)](https://pypi.org/project/rj2y/)
[![PyPI Python Versions](https://img.shields.io/pypi/pyversions/rj2y)](https://pypi.org/project/rj2y/)
[![Downloads](https://pepy.tech/badge/rj2y)](https://pepy.tech/project/rj2y)

This CLI tool is a simple utility to convert JSON to YAML. Especially useful when you want to convert JSON including JSON-embedded string.

```json
{
  "iii": "{\"i\":\"{\\\"ii\\\": \\\"ii\\\"}\",\"ii\":\"ii\"}",
  "kkk": "{\"k\": \"{\\\"kk\\\": \\\"kk1\\\\nkk2\\\\nkk3\\\\n\\\"}\"}"
}
```

```yaml
iii:
  i:
    ii: !!str ii
  ii: !!str ii
kkk:
  k:
    kk: !!str |-
      kk1
      kk2
      kk3
```

It may be convenient to reading server logs. Using with [`jq`](https://github.com/jqlang/jq) and [`yq`](https://github.com/mikefarah/yq) is recommended.

## Installation

```bash
pipx install rj2y
```

## Usage

```bash
cat some.json | rj2y
rj2y some.json
```

### Example

input json and output yaml

<https://github.com/pollenjp/rj2y-py/blob/d237729c54be84f1dd78542bf4bd2476c7a16e3a/tests/unittest/test_main.py#L6-L39>

<https://github.com/pollenjp/rj2y-py/blob/d237729c54be84f1dd78542bf4bd2476c7a16e3a/tests/unittest/test_main.py#L45-L109>

Using yq make it easier to read.

```sh
cat some.json | rj2y | yq
```

```yaml
aaa: !!str AAA
bbb: !!bool true
ccc: !!int 123
ccc2: !!str 123
ddd: !!float 123.456
ddd2: !!str 123.456
eee:
  - !!str e
  - !!str ee
  - !!str eee
fff:
  f: !!str f
  ff: !!str ff
  fff: !!str fff
ggg:
  - g: !!str g
    gg: !!str gg
    ggg: !!str ggg
  - g: !!str g
    gg: !!str gg
    ggg: !!str ggg
hhh:
  h: !!str h
  hh: !!str hh
  hhh: !!str hhh
iii:
  i:
    ii: !!str ii
  ii: !!str ii
jjj: !!str |-
  jj1
  jj2
  jj3
kkk:
  k:
    kk: !!str |-
      kk1
      kk2
      kk3
```
