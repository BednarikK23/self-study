#include <iostream>
#include <list>
#include <limits>
#include <functional>
#include <algorithm>
#include <cctype>
#include <locale>

using std::string, std::endl, std::cout, std::cin;

class TodoItem {
private:
    int id;
    string description;
    bool completed;

public:
    TodoItem() : id(0), description(""), completed(false) {}
    ~TodoItem() = default;

    bool create(string new_description) {
        id = rand() % 100 + 1;  // random number between 1 and 100
        description = new_description;
        return true;
    }

    void setDescription(string new_description) {
        description = new_description;
    }

    void setCompleted(bool new_completed) {
        completed = new_completed;
    }

    int getId() const { return id; }
    string getDescription() { return description; }
    bool isCompleted() const { return completed; }
};


// trim from start (in place)
static inline void ltrim(std::string &s) {
    s.erase(s.begin(), std::find_if(s.begin(), s.end(), [](unsigned char ch) {
        return !std::isspace(ch);
    }));
}

void edit_task(std::_List_iterator<TodoItem> &it) {
    string new_description;
    cout << "Enter a new description: ";
    cin.ignore();
    std::getline(cin, new_description);
    it->setDescription(new_description);
}


void complete_task(std::_List_iterator<TodoItem> &it) {
    it->setCompleted(true);
}

void find_and_do(std::list <TodoItem> &todoItems, const std::function<void(std::_List_iterator<TodoItem>&)> &func) {
    int id;
    cin >> id;
    if(!cin) // or if(cin.fail())
    {
        // user didn't input a number
        cin.clear(); // reset failbit
        cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); //skip bad input
        // next, request user reinput
    }

    std::list <TodoItem>::iterator it;
    for (it = todoItems.begin(); it != todoItems.end(); it++) {
        if (it->getId() == id) {
            if (func == nullptr) {
                todoItems.erase(it);
                return;
            }
            func(it);
            break;
        }
    }
}

int main() {
    std::list <TodoItem> todoItems;
    std::list <TodoItem>::iterator it;
    string input_option;

    srand(time(NULL));
    todoItems.clear();

    TodoItem test;
    test.create("test");
    todoItems.push_back(test);

    while (1) {
        //system("clear");  // clear screen

        cout << "Todo List Maker" << endl;
        cout << endl << endl;
        for (it = todoItems.begin(); it != todoItems.end(); it++) {
            string curr_mode = it->isCompleted() ? "done" : "not done";
            cout << it->getId() << " | " << it->getDescription() << " | " << curr_mode << endl;
        }

        if (todoItems.empty()) {
            cout << "Add todo!" << endl;
        }

        cout << "[a]dd a new Todo" << endl;
        cout << "[c]omplete a Todo" << endl;
        cout << "[d]elete a Todo" << endl;
        cout << "[e]dit a Todo" << endl;
        cout << "[q]uit" << endl;


        cin >> input_option;
        ltrim(input_option);
        if (input_option[0] == 'q') {
            cout << "bye!" << endl;
            break;
        } else if (input_option[0] == 'a') {
            TodoItem new_item;
            string new_description;

            cout << "Enter a description: ";
            cin.ignore();
            std::getline(cin, new_description);

            new_item.create(new_description);

            todoItems.push_back(new_item);
        } else if (input_option[0] == 'c') {
            cout << "Enter the id of the Todo to complete: ";

            find_and_do(todoItems, complete_task);
        } else if (input_option[0] == 'd') {
            cout << "Enter the id of the Todo to delete: ";

            find_and_do(todoItems, nullptr);
        } else if (input_option[0] == 'e') {
            cout << "Enter the id of the Todo to edit: ";

            find_and_do(todoItems, edit_task);
        } else {
            cout << "Invalid option!" << endl;
        }
    }

    return 0;
}
