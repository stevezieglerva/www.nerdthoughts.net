---
layout: post
tags: continuous delivery
---


- shard big long updates into sections to avoid long locking
- split DB updates into steps
- delete columns later with maintenance steps
- delete column stop reading, but still writing
