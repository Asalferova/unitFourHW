const {BookService} = require('./script.js');
  
describe('BookService', () => {
  let bookRepository;
  let bookService;

  beforeEach(() => {
    // Создаем мок-объект BookRepository
    bookRepository = {
      getBooks: jest.fn(),
      getBookById: jest.fn(),
    };

    // Создаем экземпляр класса BookService с использованием мок-объекта
    bookService = new BookService(bookRepository);
  });

  describe('getBooks', () => {
    it('should return an array of books', () => {
      // Задаем ожидаемое значение для мок-метода getBooks
      bookRepository.getBooks.mockReturnValue(['Book 1', 'Book 2', 'Book 3']);

      // Вызываем метод getBooks и проверяем ожидаемый результат
      const books = bookService.getBooks();
      expect(books).toEqual(['Book 1', 'Book 2', 'Book 3']);
    });
  });

  describe('getBookById', () => {
    it('should return the book with the specified id', () => {
      // Задаем ожидаемое значение для мок-метода getBookById
      bookRepository.getBookById.mockReturnValue('Book 1');

      // Вызываем метод getBookById с указанным id и проверяем ожидаемый результат
      const book = bookService.getBookById(1);
      expect(book).toEqual('Book 1');
    });
  });

});