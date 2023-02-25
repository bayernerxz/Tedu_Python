import asyncio
import time


# 定义协程函数
async def fun1():
    print("start1")
    # 设置跳转的阻塞点
    await asyncio.sleep(2)
    print("end1")


async def fun2():
    print("start2")
    await asyncio.sleep(3)
    print("end2")


tm = time.time()

# 生成协程对象
cor1 = fun1()
cor2 = fun2()

tasks = [asyncio.ensure_future(cor1), asyncio.ensure_future(cor2)]  # 这种方法已经在3.10中弃用
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

print(time.time() - tm)
