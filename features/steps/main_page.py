from behave import given, when, then


@given('Open main page')
def open_main_page(context):
    context.app.main_page.open_main_page()


@when('Click on search icon')
def click_on_search_icon(context):
    context.app.main_page.click_on_search_icon()


@when('Search for the {product}')
def search_for_product(context, product):
    context.app.main_page.search_for_product(product)


@then('Verify each footer policy link opens correct page')
def verify_policy_links(context):
    context.app.main_page.verify_policy_links()
