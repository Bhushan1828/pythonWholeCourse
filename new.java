import java.util.*;
import java.util.stream.Collectors;

class Data {
    String category;
    String subCategory;
    double value;

    // Constructor to initialize fields
    public Data(String category, String subCategory, double value) {
        this.category = category;
        this.subCategory = subCategory;
        this.value = value;
    }
}

class GroupAndAverage {
    public static Map<String, Map<String, Double>> groupAndAverage(List<Data> dataList) {
        if (dataList == null || dataList.isEmpty()) {
            throw new IllegalArgumentException("Input must be a non-empty list");
        }

        return dataList.stream()
                .collect(Collectors.groupingBy(
                        data -> data.category,
                        Collectors.groupingBy(
                                data -> data.subCategory,
                                Collectors.averagingDouble(data -> data.value)
                        )
                ));
    }

    public static void main(String[] args) { // Corrected main method signature
        List<Data> dataList = Arrays.asList(
                new Data("Fruit", "Apple", 10),
                new Data("Fruit", "Apple", 20),
                new Data("Fruit", "Banana", 5),
                new Data("Vegetable", "Carrot", 15),
                new Data("Vegetable", "Carrot", 25),
                new Data("Vegetable", "Spinach", 3)
        );
        Map<String, Map<String, Double>> result = groupAndAverage(dataList);
        System.out.println(result);
        // Expected output:
        // {Fruit={Apple=15.0, Banana=5.0}, Vegetable={Carrot=20.0, Spinach=3.0}}
   }
}
