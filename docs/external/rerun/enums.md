---
source: https://ref.rerun.io/docs/python/stable/common/enums
title: Enums
---

# Enums



### rerun



#### classBox2DFormat



Bases: `Enum`



How to specify 2D boxes (axis-aligned bounding boxes).



##### XCYCW2H2='XCYCW2H2'class-attributeinstance-attribute



[x_center, y_center, width/2, height/2].



##### XCYCWH='XCYCWH'class-attributeinstance-attribute



[x_center, y_center, width, height].



##### XYWH='XYWH'class-attributeinstance-attribute



[x,y,w,h], with x,y = left,top.



##### XYXY='XYXY'class-attributeinstance-attribute



[x0, y0, x1, y1], with x0,y0 = left,top and x1,y1 = right,bottom.



##### YXHW='YXHW'class-attributeinstance-attribute



[y,x,h,w], with x,y = left,top.



##### YXYX='YXYX'class-attributeinstance-attribute



[y0, x0, y1, x1], with x0,y0 = left,top and x1,y1 = right,bottom.