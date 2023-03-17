# ykenan_log

> **`Print and save a simple log to a file`**

## Use

> install

```shell
pip install coloredlogs
pip install ykenan_log
```

> use

```python
# -*- coding: utf-8 -*-

import ykenan_log

logger = ykenan_log.Logger("name", "log")

if __name__ == '__main__':
    print("run...")
    logger.debug("info......")
    logger.info("info......")
    logger.warn("info......")
    logger.error("info......")
```

> output

```shell
run...
2023-03-17 09:21:36 root name[34768] DEBUG info......
2023-03-17 09:21:36 root name[34768] INFO info......
2023-03-17 09:21:36 root name[34768] WARNING info......
2023-03-17 09:21:36 root name[34768] ERROR info......

```
