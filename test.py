import matplotlib.font_manager
sorted([f.name for f in matplotlib.font_manager.fontManager.ttflist if f.name.startswith("Apple")])