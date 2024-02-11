#!/usr/bin/python3
""" __inti__ magic method for models directory"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
