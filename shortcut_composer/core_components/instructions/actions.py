# SPDX-FileCopyrightText: © 2022-2026 Wojciech Trybus <wojtryb@gmail.com>
# SPDX-License-Identifier: GPL-3.0-or-later

from dataclasses import dataclass

from api_krita.enums import Action
from ..instruction_base import Instruction


@dataclass
class ActivateOnPress(Instruction):
    """Activate a Krita action when the shortcut key is pressed."""

    action: Action

    def on_key_press(self) -> None:
        """Trigger the configured Krita action."""
        self.action.activate()


@dataclass
class ActivateOnRelease(Instruction):
    """Activate a Krita action whenever the shortcut key is released."""

    action: Action

    def on_every_key_release(self) -> None:
        """Trigger the configured Krita action."""
        self.action.activate()
