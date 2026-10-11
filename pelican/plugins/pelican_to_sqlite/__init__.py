"""Pelican plugin that exports posts to a SQLite database."""

from .pelican_to_sqlite import register

__all__ = ["register"]
