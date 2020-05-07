# TPZ
Використовуючи мову програмування Python було реалізовано клас Formuls, в якому є методи для введення даних, для обраховування введених даних за певними формулами та передбачена обробка виключних випадків для забезпечення стабільної роботи класу у випадку введення невірних даних. Згідно з варіантом, необхідними даними для коректної роботи програми є число типу float в діапазоні 57.59>= x <= 2.409. Дробові числа потрібно вводити через крапку. Результат має виводитись у вигляді числа типу float. Некоректними будуть вважатися такі дані:
	числа більші 2.409 та менші 57.59 ;
	число з стороннім символами;
	числа з табуляцією або пробілом;
	числа з комою;
	стороні символи .
У ході написання програми використано такі класи та методи:
Клас Formuls – клас, який призначений для обчислення наступних формул:
	y = x ^ 4 * 3.75 + x ^ 3 * 2.272 - x ^ 2 * 5.351 + x * 4.653 
	y = x ^ 3 * 3.37 - x ^ 2 * 3.336 + x * 5.42
	y = x ^ 2 * 1.441 + x * 2.465
	y = x * 6.364
Метод def formul_1 – обчислює значення формули y = x ^ 4 * 3.75 + x ^ 3 * 2.272 - x ^ 2 * 5.351 + x * 4.653, куди підставляється значення «х», який ми задаємо в конструкторі def __init__.
Метод def formul_2 – обчислює значення формули y = x ^ 3 * 3.37 - x ^ 2 * 3.336 + x * 5.42, куди також підставляється значення «х».
Метод def formul_3 – обчислює значення формули y = x ^ 2 * 1.441 + x * 2.465, куди підставляється значення «х».
Метод def formul_4 – обчислює значення формули y = x * 6.364, куди підставляється значення «х».
Для обробки винятків використано конструкцію try/except, яка необхідна для того, щоб повідомляти про помилки. А саме генеруються винятки ValueError, операція, що застосовується до об’єктів невідповідного типу. Також були створені два класи для обробки винятків. Класс NonPositiveError() для обробки від’ємних чисел та клас WrongRangeX() для обробки чисел, що не входять в діапазон Х.
