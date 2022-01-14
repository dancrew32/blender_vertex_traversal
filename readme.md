# Blender Vertex Traversal

I asked this on the blender stack exchange and decided to try building it myself:
https://blender.stackexchange.com/q/249709/70346

Sometimes you are working with a string or path and you want to conveniently select the next or previous vertex. This plugin works by picking the next or previous available vertex in a mesh during edit mode.

## Requirements
Blender 3.0.0+ (Tested in LTS)

## Installation
1. Download Latest Release https://github.com/dancrew32/blender_vertex_traversal/archive/refs/tags/v1_2.zip
2. Edit > Preferences > Add-ons > Install > blender_vertex_traversal-1_2.zip
3. Enable "Vertex Traversal" add-on.
4. Observe "Vertex Traversal" panel in 3D View during Edit Mode (see usage).

## Usage

1. Select an object and change to edit mode.
2. Open the "Vertex Traversal" panel
3. Select Next or Prev to cycle through the vertices (aka `vertex.prev` or `vertex.next`)
4. Pro-tip: Right click "Prev Vertex" and "Next Vertex" then save them to Quick Favorites. Then hit Q while editing for a convenient way to select the next and previous vertices!

