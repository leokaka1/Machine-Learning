from jsonpath import jsonpath

book_dict = {
  "store": {
    "book": [
      { "category": "reference",
        "author": "Nigel Rees",
        "title": "Sayings of the Century",
        "price": 8.95
      },
      { "category": "fiction",
        "author": "Evelyn Waugh",
        "title": "Sword of Honour",
        "price": 12.99
      },
      { "category": "fiction",
        "author": "Herman Melville",
        "title": "Moby Dick",
        "isbn": "0-553-21311-3",
        "price": 8.99
      },
      { "category": "fiction",
        "author": "J. R. R. Tolkien",
        "title": "The Lord of the Rings",
        "isbn": "0-395-19395-8",
        "price": 22.99
      }
    ],
    "bicycle": {
      "color": "red",
      "price": 19.95
    }
  }
}

# 找到store中所有的book的作者
author = jsonpath(book_dict,'$.store.book[*].author')
print(author)

# 所有的作者
all_author = jsonpath(book_dict,'$..author')
print(all_author)

# store下所有的元素
all_element = jsonpath(book_dict,'$.store.*')
print(all_element)

# store下所有内容的价格
all_price = jsonpath(book_dict,'$.store..price]')
print(all_price)

# 第三本数
thir_book = jsonpath(book_dict,'$..book[2]')
print(thir_book)

# 最后一本书
# '$..book[(@length-1)]'
last_book = jsonpath(book_dict,'$..book[-1:]')
print(last_book)

# 前两本书
# '$book[:2]'
begin_two = jsonpath(book_dict,'$..book[0,1]')
print(begin_two)

# 获取有isbn的所有书
isbn = jsonpath(book_dict,'$..book[?(@.isbn)]')
print(isbn)

# 获取价格大于10的所有书
above_10 = jsonpath(book_dict,'$..book[?(@.price<10)]')
print(above_10)

# 获取所有数据
all = jsonpath(book_dict,"$..*")
print(all)