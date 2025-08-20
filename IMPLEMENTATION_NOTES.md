# Default City Buttons Implementation

## Changes Made

Added three default city buttons to the pyweather GUI application:
- **Cupertino** button
- **New York** button  
- **London** button

## Implementation Details

### New Functions Added:
```python
def set_cupertino():
    user_input_city.delete(0, END)
    user_input_city.insert(0, "Cupertino")

def set_newyork():
    user_input_city.delete(0, END)
    user_input_city.insert(0, "New York")

def set_london():
    user_input_city.delete(0, END)
    user_input_city.insert(0, "London")
```

### New UI Elements:
```python
# Default city buttons
Button(root, text="Cupertino", command=set_cupertino, width=10).grid(row=3, column=1)
Button(root, text="New York", command=set_newyork, width=10).grid(row=3, column=2)
Button(root, text="London", command=set_london, width=10).grid(row=3, column=3)
```

## Layout Changes

The buttons are positioned in row 3 of the grid layout:
- Row 0: Application title
- Row 1: City input field, temperature units, OK button
- Row 2: Display mode (Simple/Advanced) radio buttons
- **Row 3: Default city buttons (NEW)**

## Functionality

Each button, when clicked:
1. Clears the current city input field
2. Sets the field to the corresponding city name
3. User can then click OK to fetch weather for that city

## Testing

- ✅ All functions work correctly
- ✅ Buttons properly set city input field values
- ✅ No syntax errors in the code
- ✅ Minimal changes made (17 lines added, 0 deleted)