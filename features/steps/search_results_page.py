from behave import then


@then('Verify the results have {product}')
def verify_search_results(context, product):
    context.app.search_results_page.verify_search_results(product)
