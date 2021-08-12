import asyncio


async def func(i: int):
    # on place la boucle au sein de la fonction elle-même
    while True:
        await asyncio.sleep(i)
        print(f"I waited {i} seconds")


async def main():

    # si on fait comme la ligne ci-dessous 
    # on attend l'execution de chaque coroutines avant d'executer la suivante
    # mais on avancera jamais à 4 secondes car le While True prend précédence
    # [await func(5 - i) for i in range(0, 5)]

    # ici on crée une liste de coroutines à exécuter
    tasks = [asyncio.create_task(func(10 - i)) for i in range(0, 10)]

    # puis on les lance en même temps (chaque ligne ci-dessous est un synonyme)
    [await task for task in tasks]
    # await asyncio.gather(*tasks)
    # [await asyncio.ensure_future(task) for task in tasks]
    
    # comme elles sont lancées en parallèle et que ce sont des tasks
    # elle s'éxécutent bien en asynchrone côte à côte.
    # du coup il ne reste qu'à définir une condition globale qui permet de sortir
    # de la boucle While True

    # c'est du vrai asynchrone, c'est pour ça que la coroutine 1sc finit avant les autres
    # meme si elle st appelée en dernier ( 10 - i )


if __name__ == "__main__":
    asyncio.run(main())