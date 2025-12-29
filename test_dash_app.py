import dash
from dash import html, dcc

# Import your Dash app
from dash_app import app


def find_component(component, component_type):
    """Recursively search Dash layout for a component type"""
    if isinstance(component, component_type):
        return True

    if hasattr(component, "children"):
        children = component.children
        if isinstance(children, list):
            return any(find_component(child, component_type) for child in children)
        return find_component(children, component_type)

    return False


def test_header_present():
    layout = app.layout
    assert find_component(layout, html.H1), "Header (H1) not found"


def test_visualisation_present():
    layout = app.layout
    assert find_component(layout, dcc.Graph), "Graph not found"


def test_region_picker_present():
    layout = app.layout
    assert find_component(layout, dcc.RadioItems), "Region picker not found"