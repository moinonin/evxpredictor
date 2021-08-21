from evxpredictor import mlbot
from concurrent.futures import ThreadPoolExecutor
import time, asyncio


async def runner(alpha,sig):
	with ThreadPoolExecutor(max_workers=2) as executor:
		futures = executor.submit(mlbot.signal, 20,65,120,alpha,f'{sig}')
		return futures.result()


start = time.perf_counter()
print(asyncio.run(runner(0.0025,'sell')))
end = time.perf_counter()

print(f'{end -start}' + ' seconds')




