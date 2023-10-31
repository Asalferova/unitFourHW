class BookService {
    constructor(bookRepository) {
      this.bookRepository = bookRepository;
    }
  
    getBooks() {
      return this.bookRepository.getBooks();
    }
  
    getBookById(id) {
      return this.bookRepository.getBookById(id);
    }
  }
  
  module.exports = {BookService};
  
  