/**
 * Дана строка (возможно, пустая), состоящая из букв A-Z и пробелов, разделяющих слова:
 * "QUICK FOX   JUMPS"
 * Нужно написать функцию, которая развернет слова:
 * "KCIUQ XOF   SPMUJ"
 * И сгенерирует ошибку, если на вход пришла невалидная строка.
 */

 // "  AB  " -> "  BA  "

 public String revertWords(String str) {
    // your code
    checkValid(str);
    final StringBuilder result = new StringBuilder();
    int i = 0;
    while (i < str.lentgh()) {
        final char c = str.charAt(i);
        if (c == ' ') {
            result.append(c);
            i++;
        } else {
            final nextSegment = getNextSegment(str, i);
            result.append(nextSegment);
            i += nextSegment.length();
        }
    }

    return result.toString();
}

String getNextSegment(String source, int offset) {
    final SringBuilder temp = new StringBuilder();
    int i = offset;
    char c;
    while (i < source.lentgh()) {
        c = str.charAt(i);
        if (c == ' ') {
            break;
        }
        checkChar(c);
        temp.appent(c);
        i++;
    }

    return temp.reverse();
}

private checkChar(char c) {
    if (c < 'A' || c > 'Z') {
        throw new IllegalArgumentException("Must be 'A' - 'Z'");
    }
}


@Test
public void testRevertEmptySource() {
    assertEquals("", revertWords(""));
}

@Test
public void testRevertOnlySpaces() {
    assertEquals(" ", revertWords(" "));
    assertEquals("  ", revertWords("  "));
    assertEquals("   ", revertWords("   "));
}

@Test
public void testRevertValidSimpleSource() {
    assertEquals("  BA  ", revertWords("  AB  "));
}

@Test
public void testRevertValidSimpleSource() {
    assertEquals("BA  ", revertWords("AB  "));
}


@Test(expected=IllegalArgumentException.class)
public void testRevertSourceWithInvalidChars() {
    revertWords("123aa");
}
