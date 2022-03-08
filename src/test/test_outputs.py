import unittest
import sys
import io

sys.path.append("src")
import outputs_web


class TestUtils(unittest.TestCase):
    def test_header(self):
        print("test_header")
        captured_output = io.StringIO()
        sys.stdout = captured_output
        outputs_web.Header.header()
        sys.stdout = sys.__stdout__
        expected_result = "################## Full Cycle Store ################## \n\n"
        self.assertEqual(captured_output.getvalue(), expected_result)

    def test_list(self):
        print("test_list")
        captured_output = io.StringIO()
        sys.stdout = captured_output
        outputs_web.List.list()
        sys.stdout = sys.__stdout__
        expected_result = "Lista de produtos da loja \n\n"
        self.assertEqual(captured_output.getvalue(), expected_result)

    def test_which_product(self):
        print("which_product")
        actual_result = outputs_web.InputsQuestions.which_product()
        expected_result = "\nQual produto você gostaria de comprar?\n"
        self.assertEqual(actual_result, expected_result)

    def test_which_amount(self):
        print("which_amount")
        actual_result = outputs_web.InputsQuestions.which_amount()
        expected_result = "Qual a quantidade deste produto deseja comprar? \n"
        self.assertEqual(actual_result, expected_result)

    def test_keep_purchase_inputs(self):
        print("keep_purchase")
        actual_result = outputs_web.InputsQuestions.keep_purchase()
        expected_result = (
            "Você deseja continuar suas compras? Digite 's' para sim ou 'n' para não \n"
        )
        self.assertEqual(actual_result, expected_result)

    def test_your_purchase(self):
        print("your_purchase")
        captured_output = io.StringIO()
        sys.stdout = captured_output
        outputs_web.CartPurchase.your_purchase()
        sys.stdout = sys.__stdout__
        expected_result = (
            "Esta é a sua compra. Obrigado por comprar com a Full Cycle Store!\n\n"
        )
        self.assertEqual(captured_output.getvalue(), expected_result)

    def test_purchase_details(self):
        print("purchase_details")
        captured_output = io.StringIO()
        sys.stdout = captured_output
        outputs_web.CartPurchase.purchase_details("name", 1, 1, 1)
        sys.stdout = sys.__stdout__
        expected_result = (
            "     Item: name, quantidade 1, valor unitário 1.00, subtotal 1.00\n"
        )
        self.assertEqual(captured_output.getvalue(), expected_result)

    def test_total_purchase(self):
        print("total_purchase")
        captured_output = io.StringIO()
        sys.stdout = captured_output
        outputs_web.CartPurchase.total_purchase(2)
        sys.stdout = sys.__stdout__
        expected_result = "\nO valor total da compra: 2.00\n"
        self.assertEqual(captured_output.getvalue(), expected_result)

    def test_keep_purchase(self):
        print("keep_purchase")
        captured_output = io.StringIO()
        sys.stdout = captured_output
        outputs_web.CartPurchase.keep_purchase()
        sys.stdout = sys.__stdout__
        expected_result = "Selecione o produto conforme a lista abaixo\n"
        self.assertEqual(captured_output.getvalue(), expected_result)

    def test_input_product(self):
        print("input_product")
        captured_output = io.StringIO()
        sys.stdout = captured_output
        outputs_web.InputsWarnings.input_product()
        sys.stdout = sys.__stdout__
        expected_result = "Por favor, escolha o produto entre 1 e 6\n"
        self.assertEqual(captured_output.getvalue(), expected_result)

    def test_input_amount(self):
        print("input_amount")
        captured_output = io.StringIO()
        sys.stdout = captured_output
        outputs_web.InputsWarnings.input_amount()
        sys.stdout = sys.__stdout__
        expected_result = "Por favor, escolha uma quantidade até 9 itens\n"
        self.assertEqual(captured_output.getvalue(), expected_result)

    def test_input_keep(self):
        print("input_keep")
        captured_output = io.StringIO()
        sys.stdout = captured_output
        outputs_web.InputsWarnings.input_keep()
        sys.stdout = sys.__stdout__
        expected_result = "Por favor, digite s para sim e n para não\n"
        self.assertEqual(captured_output.getvalue(), expected_result)

    def test_inventory_not_available(self):
        print("inventory_not_available")
        captured_output = io.StringIO()
        sys.stdout = captured_output
        outputs_web.InventoryCheck.inventory_not_available()
        sys.stdout = sys.__stdout__
        expected_result = "Não temos estoque suficiente para este produto.\n"
        self.assertEqual(captured_output.getvalue(), expected_result)


if __name__ == "__main__":
    unittest.main()
