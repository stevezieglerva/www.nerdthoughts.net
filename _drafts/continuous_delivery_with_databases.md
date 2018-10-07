---
layout: post
tags: elasticsearch
---


- shard big long updates into sections to avoid long locking
- split DB udates into steps
- delete columns later with maintenance steps
- delete column stop reading, but still writing
