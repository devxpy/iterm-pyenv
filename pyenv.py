import asyncio
import subprocess
import iterm2
import os

async def main(connection):
    component = iterm2.StatusBarComponent(
        short_description='pyenv',
        detailed_description='The currently active Python',
        exemplar='🐍 3.7.2',
        update_cadence=None,
        identifier='dev.pyenv',
        knobs=[],
    )

    @iterm2.StatusBarRPC
    async def pyenv_coroutine(knobs, py=iterm2.Reference('user.py?')):
        print(py)
        return f'🐍 {py}'

    await component.async_register(connection, pyenv_coroutine)

iterm2.run_forever(main)
