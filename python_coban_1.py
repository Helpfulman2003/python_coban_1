import collections # Dùng Counter để đếm cho tiện.

def problem_1_title_case(text):
    """
    1. Viết hoa chữ cái đầu mỗi từ, còn lại viết thường.
       Ví dụ: "nGuYen vAN a" -> "Nguyen Van A"
    """
    print(f"\n--- Yêu cầu 1: Viết hoa chữ cái đầu mỗi từ ---")
    print(f"Chuỗi gốc: '{text}'")

    if not text:
        print("Chuỗi rỗng.")
        return ""

    # Tách chuỗi thành các từ. Dùng split(' ') có thể tạo từ rỗng nếu nhiều khoảng trắng.
    words = text.split(' ') 
    
    title_cased_words = [] 
    for word in words:
        if word: # Bỏ qua từ rỗng
            # Chữ đầu viết hoa, còn lại viết thường.
            title_cased_word = word[0].upper() + word[1:].lower()
            title_cased_words.append(title_cased_word)
        else:
            title_cased_words.append("") # Giữ lại từ rỗng để join cho đúng cấu trúc (nếu cần)
            
    result = " ".join(title_cased_words)
    print(f"Chuỗi sau khi xử lý: '{result}'")
    return result

def problem_2_reverse_words_in_string(text):
    """
    2. Đảo ngược thứ tự các từ trong chuỗi.
       Ví dụ: "lap trinh bang ngon ngu python" -> "python ngu ngon bang trinh lap"
    """
    print(f"\n--- Yêu cầu 2: Đảo ngược thứ tự từ ---")
    print(f"Chuỗi gốc: '{text}'")
    if not text:
        print("Chuỗi rỗng.")
        return ""
    
    # text.split() tự xử lý nhiều khoảng trắng và loại bỏ từ rỗng.
    words = text.split()
    
    # Đảo ngược danh sách từ bằng slicing.
    reversed_words = words[::-1]
    
    result = " ".join(reversed_words)
    print(f"Chuỗi sau khi đảo ngược từ: '{result}'")
    return result

def problem_3_most_frequent_character(text):
    """
    3. Tìm ký tự xuất hiện nhiều nhất. Bỏ qua khoảng trắng, không phân biệt hoa/thường.
    """
    print(f"\n--- Yêu cầu 3: Ký tự xuất hiện nhiều nhất ---")
    print(f"Chuỗi gốc: '{text}'")
    if not text:
        print("Chuỗi rỗng.")
        return None, 0 

    # Chuẩn hóa chuỗi: chuyển thường, bỏ khoảng trắng.
    processed_text = text.lower().replace(" ", "")
    
    if not processed_text: 
        print("Chuỗi chỉ chứa khoảng trắng hoặc rỗng sau xử lý.")
        return None, 0
        
    # Đếm tần suất ký tự bằng Counter.
    char_counts = collections.Counter(processed_text) 
    
    if char_counts: 
        # Lấy ký tự phổ biến nhất. most_common(1) trả về list dạng [('char', count)].
        most_common_char, count = char_counts.most_common(1)[0]
        
        print(f"Ký tự '{most_common_char}' xuất hiện nhiều nhất với {count} lần.")
        return most_common_char, count
    else:
        print("Không có ký tự để đếm.")
        return None, 0


def problem_4_count_character_occurrences(text):
    """
    4. Liệt kê số lần xuất hiện của mỗi ký tự. Bỏ qua khoảng trắng, không phân biệt hoa/thường.
    """
    print(f"\n--- Yêu cầu 4: Liệt kê số lần xuất hiện của mỗi ký tự ---")
    print(f"Chuỗi gốc: '{text}'")
    if not text:
        print("Chuỗi rỗng.")
        return {} 

    # Chuẩn hóa chuỗi.
    processed_text = text.lower().replace(" ", "") 
    if not processed_text:
        print("Chuỗi chỉ chứa khoảng trắng hoặc rỗng sau xử lý.")
        return {}

    char_counts = collections.Counter(processed_text) 
    
    print("Số lần xuất hiện của mỗi ký tự:")
    # Sắp xếp theo ký tự cho dễ nhìn.
    for char, count in sorted(char_counts.items()):
        print(f"Ký tự '{char}': {count} lần")
    return dict(char_counts) 

def problem_5_check_and_extract_numbers(text):
    """
    5. Kiểm tra chuỗi có ký tự số không. Nếu có, tách các chữ số ra list.
       Ví dụ: "abc123xyz45" -> True, ['1', '2', '3', '4', '5']
    """
    print(f"\n--- Yêu cầu 5: Kiểm tra và tách ký tự số ---")
    print(f"Chuỗi gốc: '{text}'")
    
    digits_list = [] 
    has_digit = False  

    if not isinstance(text, str): 
        print("Đầu vào không phải chuỗi.")
        return False, [] 

    for char in text: 
        if char.isdigit(): # Kiểm tra ký tự có phải số không.
            has_digit = True 
            digits_list.append(char) 
    
    if has_digit:
        print(f"Chuỗi có ký tự số. Các ký tự số: {digits_list}")
    else:
        print("Chuỗi không có ký tự số.")
    return has_digit, digits_list

def problem_6_split_full_name(full_name):
    """
    6. Cắt họ tên thành họ lót và tên.
       Ví dụ: "Nguyễn Văn An" -> ("Nguyễn Văn", "An")
    """
    print(f"\n--- Yêu cầu 6: Cắt chuỗi họ tên ---")
    print(f"Họ tên gốc: '{full_name}'")

    # Bỏ khoảng trắng thừa ở đầu/cuối rồi tách từ.
    if not full_name or not full_name.strip(): 
        print("Chuỗi họ tên rỗng.")
        return "", "" 

    name_parts = full_name.strip().split() 
        
    if len(name_parts) == 1: # Chỉ có tên
        first_middle_name = "" 
        last_name = name_parts[0] 
    else: # Có họ lót và tên
        last_name = name_parts[-1] # Tên là từ cuối.
        first_middle_name = " ".join(name_parts[:-1]) # Còn lại là họ lót.
        
    print(f"Họ lót: '{first_middle_name}', Tên: '{last_name}'")
    return first_middle_name, last_name

def problem_7_capitalize_first_letter_of_each_word(text):
    """
    7. Chuyển ký tự đầu mỗi từ thành chữ hoa (giống Yêu cầu 1).
       Ví dụ: "học lập trình python" -> "Học Lập Trình Python"
    """
    print(f"\n--- Yêu cầu 7: Viết hoa chữ cái đầu mỗi từ ---")
    print(f"Chuỗi gốc: '{text}'")
    if not text:
        print("Chuỗi rỗng.")
        return ""
    
    # Cách 1: Dùng hàm title() sẵn có (ngắn gọn).
    # result = text.title() 
    
    # Cách 2: Làm thủ công (giống problem_1_title_case).
    words = text.split(' ') 
    capitalized_words = []
    for word in words:
        if word: 
            capitalized_word = word[0].upper() + word[1:].lower() 
            capitalized_words.append(capitalized_word)
        else:
            capitalized_words.append("") 
            
    result = " ".join(capitalized_words)
    print(f"Chuỗi sau khi viết hoa chữ cái đầu mỗi từ: '{result}'")
    return result

def problem_8_alternating_case(text):
    """
    8. Đổi chữ xen kẽ hoa/thường. Bỏ qua ký tự không phải chữ cái khi xét xen kẽ.
       Ví dụ: "ABCDEfgh" -> "AbCdEfGh"
    """
    print(f"\n--- Yêu cầu 8: Đổi chữ xen kẽ hoa thường ---")
    print(f"Chuỗi gốc: '{text}'")
    if not text:
        print("Chuỗi rỗng.")
        return ""
        
    result = [] 
    # Cờ is_next_upper: True nếu chữ cái tiếp theo là HOA.
    is_next_upper = True 
    
    for char in text: 
        if char.isalpha(): # Chỉ xử lý chữ cái.
            if is_next_upper:
                result.append(char.upper()) 
            else:
                result.append(char.lower()) 
            is_next_upper = not is_next_upper # Đảo cờ cho chữ cái sau.
        else:
            result.append(char) # Giữ nguyên ký tự không phải chữ cái.
            
    final_result = "".join(result) 
    print(f"Chuỗi sau khi đổi chữ xen kẽ: '{final_result}'")
    return final_result

def problem_9_is_palindrome(text):
    """
    9. Kiểm tra chuỗi đối xứng (palindrome). 
       Bỏ qua khoảng trắng, ký tự đặc biệt, không phân biệt hoa/thường.
       Ví dụ: "Madam" -> True
    """
    print(f"\n--- Yêu cầu 9: Kiểm tra chuỗi đối xứng (Palindrome) ---")
    print(f"Chuỗi gốc: '{text}'")

    if text is None: 
        print("Đầu vào là None.")
        return False

    # Chuẩn hóa chuỗi: chỉ giữ chữ và số, chuyển thành chữ thường.
    # filter(str.isalnum, text) lọc ra các ký tự là chữ hoặc số.
    processed_text = "".join(filter(str.isalnum, text)).lower()
    
    if not processed_text: # Chuỗi rỗng (sau xử lý) coi là đối xứng.
        print("Chuỗi rỗng sau xử lý, coi là đối xứng.")
        return True 

    # So sánh chuỗi đã xử lý với chuỗi đảo ngược của nó.
    reversed_text = processed_text[::-1] 
    
    if processed_text == reversed_text:
        print(f"Chuỗi '{text}' (xử lý thành '{processed_text}') LÀ chuỗi đối xứng.")
        return True
    else:
        print(f"Chuỗi '{text}' (xử lý thành '{processed_text}') KHÔNG LÀ chuỗi đối xứng.")
        return False

def problem_10_describe_three_digit_number(number_str):
    """
    10. Nhập số có 3 chữ số (dạng chuỗi), xuất ra cách đọc tiếng Việt.
        Ví dụ: "123" -> "một trăm hai mươi ba"
    """
    print(f"\n--- Yêu cầu 10: Mô tả số có 3 chữ số ---")
    print(f"Số gốc (dạng chuỗi): '{number_str}'")

    # Kiểm tra đầu vào.
    if not (isinstance(number_str, str) and len(number_str) == 3 and number_str.isdigit()):
        print("Đầu vào không phải chuỗi số có 3 chữ số.")
        return "Đầu vào không hợp lệ"

    digits_map = {
        '0': "không", '1': "một", '2': "hai", '3': "ba", '4': "bốn", 
        '5': "năm", '6': "sáu", '7': "bảy", '8': "tám", '9': "chín"
    }
    
    h_char, t_char, u_char = number_str[0], number_str[1], number_str[2]
    h, t, u = int(h_char), int(t_char), int(u_char)
    
    parts = [] 
    
    # 1. Hàng trăm:
    parts.append(digits_map[h_char])
    parts.append("trăm")
    
    # 2. Hàng chục và đơn vị:
    if t == 0: # Chục là 0 (vd: 101, 200)
        if u != 0: # Đơn vị khác 0 (vd: 101, 205) -> "linh X"
            parts.append("linh")
            parts.append(digits_map[u_char])
        # Nếu u == 0 (vd: 100, 200) thì không thêm gì.
    elif t == 1: # Chục là 1 (vd: 110, 111, 115) -> "mười X"
        parts.append("mười")
        if u == 1: parts.append("một")      # 111 -> "mười một"
        elif u == 5: parts.append("lăm")    # 115 -> "mười lăm"
        elif u != 0: parts.append(digits_map[u_char]) # 112, 113...
        # Nếu u == 0 (vd: 110) thì không thêm gì.
    else: # Chục >= 2 (vd: 123, 230)
        parts.append(digits_map[t_char])
        parts.append("mươi")
        if u == 1: parts.append("mốt")      # 121 -> "hai mươi mốt"
        elif u == 4 and t >= 2: parts.append("tư") # 124 -> "hai mươi tư"
        elif u == 5 and t >=1: parts.append("lăm") # 125 -> "hai mươi lăm"
        elif u != 0: parts.append(digits_map[u_char]) # 123, 126...
        # Nếu u == 0 (vd: 120) thì không thêm gì.
            
    result_str = " ".join(parts) 
    
    if number_str == "000":
        result_str = "không trăm"
    
    print(f"Mô tả số: '{result_str}'")
    return result_str